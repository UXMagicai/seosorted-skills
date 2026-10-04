#!/usr/bin/env node
// Validates every skills/<name>/SKILL.md: frontmatter present, name matches folder,
// description within limits, body small enough to load cheaply, and relative links resolve.
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const skillsDir = join(root, "skills");
const MAX_DESC = 1024;
const MAX_BODY_TOKENS = 5000;
let failures = 0;
const fail = (skill, msg) => { failures++; console.error(`✗ ${skill}: ${msg}`); };

for (const name of readdirSync(skillsDir).sort()) {
  const dir = join(skillsDir, name);
  if (!statSync(dir).isDirectory()) continue;
  const file = join(dir, "SKILL.md");
  if (!existsSync(file)) { fail(name, "missing SKILL.md"); continue; }
  const text = readFileSync(file, "utf8");
  const m = text.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) { fail(name, "missing YAML frontmatter"); continue; }
  const [, fm, body] = m;
  const field = (k) => fm.match(new RegExp(`^${k}:\\s*(.+)$`, "m"))?.[1]?.trim();
  const fmName = field("name");
  const desc = field("description");
  if (fmName !== name) fail(name, `frontmatter name "${fmName}" must match folder`);
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(name) || name.length > 64) fail(name, "name must be kebab-case, ≤64 chars");
  if (!desc) fail(name, "missing description");
  else if (desc.length > MAX_DESC) fail(name, `description ${desc.length} chars > ${MAX_DESC}`);
  const tokens = Math.ceil(body.length / 4);
  if (tokens > MAX_BODY_TOKENS) fail(name, `body ~${tokens} tokens > ${MAX_BODY_TOKENS}`);
  for (const [, href] of body.matchAll(/\]\((?!https?:|#|mailto:)([^)]+)\)/g)) {
    if (!existsSync(join(dirname(file), href))) fail(name, `broken relative link ${href}`);
  }
  if (!failures) console.log(`✓ ${name} (~${tokens} tokens)`);
}

for (const f of [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".mcp.json"]) {
  try { JSON.parse(readFileSync(join(root, f), "utf8")); } catch (e) { fail(f, `invalid JSON: ${e.message}`); }
}

if (failures) { console.error(`\n${failures} problem(s)`); process.exit(1); }
console.log("\nAll skills valid.");
