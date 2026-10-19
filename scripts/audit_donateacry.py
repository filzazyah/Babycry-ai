#!/usr/bin/env python3
"""Local inventory for Donate-a-Cry. No audio is uploaded or copied."""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

LABELS = {"hu":"hungry_reported","bu":"burping_reported","bp":"belly_pain_reported",
          "dc":"discomfort_reported","ti":"tired_reported","lo":"lonely_reported",
          "ch":"cold_or_hot_reported","sc":"scared_reported","dk":"unknown_reported"}
AUDIO_EXTENSIONS = {".wav",".mp3",".m4a",".aac",".caf",".3gp",".ogg",".opus",".flac",".wma"}
TAG_RE = re.compile(r"-([a-z]{2})(?:\.[^.]+)?$", re.IGNORECASE)

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def probe_audio(path: Path, ffprobe: str | None) -> dict:
    if not ffprobe:
        return {"duration_seconds": None, "codec": None, "probe_status": "ffprobe_unavailable"}
    try:
        p = subprocess.run([ffprobe,"-v","error","-show_entries","format=duration:stream=codec_name",
                            "-of","json",str(path)], check=False, capture_output=True,
                           text=True, timeout=20)
        if p.returncode != 0:
            return {"duration_seconds": None, "codec": None, "probe_status": "probe_failed"}
        data = json.loads(p.stdout or "{}")
        raw_duration = (data.get("format") or {}).get("duration")
        try:
            duration = round(float(raw_duration), 3) if raw_duration is not None else None
        except (TypeError, ValueError):
            duration = None
        codecs = sorted({s.get("codec_name") for s in data.get("streams", []) if s.get("codec_name")})
        return {"duration_seconds": duration, "codec": ",".join(codecs) or None,
                "probe_status": "ok" if duration is not None or codecs else "no_audio_metadata"}
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return {"duration_seconds": None, "codec": None, "probe_status": "probe_failed"}

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit dataset locally; audio stays on this device.")
    parser.add_argument("corpus_dir", type=Path, help="Path to extracted Donate-a-Cry corpus")
    parser.add_argument("--output", type=Path, default=Path("dataset_audit_report.json"))
    parser.add_argument("--skip-hashes", action="store_true", help="Skip SHA-256 duplicate check")
    args = parser.parse_args()
    root = args.corpus_dir.expanduser().resolve()
    if not root.is_dir():
        parser.error("corpus_dir must be an existing directory")
    ffprobe = shutil.which("ffprobe")
    files = sorted(p for p in root.rglob("*") if p.is_file())
    audio_files = [p for p in files if p.suffix.lower() in AUDIO_EXTENSIONS]
    classes, extensions, bytes_by_ext, probe_counts = Counter(), Counter(), Counter(), Counter()
    durations, hashes = defaultdict(list), Counter()
    zero_byte = total_bytes = 0
    for path in audio_files:
        ext, size = path.suffix.lower() or "[no_extension]", path.stat().st_size
        extensions[ext] += 1
        bytes_by_ext[ext] += size
        total_bytes += size
        zero_byte += int(size == 0)
        match = TAG_RE.search(path.name)
        tag = match.group(1).lower() if match else "unparsed"
        label = LABELS.get(tag, "unparsed" if tag == "unparsed" else "unrecognized_tag")
        classes[label] += 1
        if not args.skip_hashes and size:
            hashes[sha256_file(path)] += 1
        meta = probe_audio(path, ffprobe)
        probe_counts[meta["probe_status"]] += 1
        if meta["duration_seconds"] is not None:
            durations[label].append(meta["duration_seconds"])
    duplicates = sum(n - 1 for n in hashes.values() if n > 1)
    report = {
      "report_type":"aggregate_local_dataset_inventory",
      "created_utc":datetime.now(timezone.utc).isoformat(),
      "dataset_name":"Donate-a-Cry (local folder; not independently authenticated)",
      "privacy_note":"No audio, paths, or filenames are included. Review before sharing.",
      "corpus_path_recorded":False, "ffprobe_available":bool(ffprobe),
      "hashes_checked":not args.skip_hashes,
      "counts":{"all_files_in_tree":len(files),"audio_files":len(audio_files),
                "zero_byte_audio_files":zero_byte,"total_audio_bytes":total_bytes,
                "exact_duplicate_excess_files_by_sha256":duplicates if not args.skip_hashes else None},
      "class_counts_from_filename_tags":dict(sorted(classes.items())),
      "extension_counts":dict(sorted(extensions.items())),
      "audio_bytes_by_extension":dict(sorted(bytes_by_ext.items())),
      "ffprobe_status_counts":dict(sorted(probe_counts.items())),
      "duration_summary_seconds_by_reported_label":{
        label:{"count":len(v),"min":round(min(v),3),"median":round(sorted(v)[len(v)//2],3),
               "max":round(max(v),3)} for label,v in sorted(durations.items()) if v},
      "label_note":"Filename tags are contributor-reported, not verified medical ground truth.",
      "limitations":["Filename parsing is heuristic; review aggregate counts.",
        "SHA-256 detects byte-identical files, not acoustically similar audio.",
        "A readable audio file is not proof it contains a baby cry or has a correct label.",
        "Do not use labels for diagnosis or decisions about delaying care."]
    }
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print("Audit selesai; audio tidak diunggah atau disalin.")
    print(f"Jumlah file audio: {len(audio_files)}")
    for label,count in sorted(classes.items()):
        print(f"  {label}: {count}")
    print(f"Laporan agregat: {output}")
    if not ffprobe:
        print("ffprobe tidak ditemukan; durasi/codec belum diperiksa.")
    print("Jangan commit audio, identitas, atau laporan sebelum meninjau metadata.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
