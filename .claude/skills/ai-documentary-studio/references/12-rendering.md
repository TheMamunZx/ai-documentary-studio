# Automated Rendering & Export

## Preflight
Check editor availability, FFmpeg/ffprobe versions, codecs, filters, storage, free disk space, source frame rates, resolutions, audio sample rates, subtitles, and output path. Do not assume a specific executable or codec exists.

## FFmpeg use
Use FFmpeg only when installed and suitable. Prefer a reproducible command or filter graph saved to `render_command.txt`; quote paths safely and avoid shell-injection risks. For mixed input sizes/frame rates, normalize scale/pad, frame rate, pixel format, time base, and audio sample rate deliberately before concatenation. Do not use stream-copy concat unless streams are compatible.

## Export profile
Read the project brief. Common YouTube target is 16:9 at 1920x1080, but frame rate, codec, bitrate/quality, audio codec, sample rate, and color range must match source and delivery requirements. Use settings the local encoder supports; record the exact command and tool version.

## Verification
A successful process exit is not enough. Confirm output exists, size is non-zero, `ffprobe` reads expected streams/duration/dimensions/frame rate, and playback review shows no black gaps, audio errors, or broken subtitles. Keep a checksum and render timestamp in the delivery manifest.

## Honest status
If rendering cannot run, deliver the editable timeline/render instructions and mark final MP4 as blocked/not created. Never create an empty placeholder named `final.mp4`.
