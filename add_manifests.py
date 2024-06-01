from pathlib import Path
import re

# Options to add to each window (separate with commas)
window_options = "imageToolsEnabled: true"

js = Path("src/index.js").read_text()
mfs = []
# Keep any manifests already in the config
if match := re.search(r"windows: \[(.*?)\]", js):
    mfs.append(match.group(1))
# Add local manifests
for mf in Path("manifests").glob("*.json"):
    mfs.append(f"{{{window_options}, manifestId: 'manifests/{mf.name}'}}")
# Add manifest urls
with Path("manifest_urls.txt").open("r") as mf_urls:
    for url in mf_urls:
        if url.startswith("http"):
            mfs.append(f"{{{window_options}, manifestId: '{url.strip()}'}}")
# Join all the manifests together in a single string
mf_str = rf"windows: [{', '.join([m for m in mfs if m])}]"
# Insert the string in the config
js = re.sub(r"windows: \[.*?\]", mf_str, js, flags=re.DOTALL)
Path("src/index.js").write_text(js)