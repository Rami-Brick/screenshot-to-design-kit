#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import os from 'os';

const SKILL_NAME = 'screenshot-to-design-kit';

function parseArgs(argv) {
  const args = { force: false, dryRun: false, customPath: null };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--force') args.force = true;
    else if (argv[i] === '--dry-run') args.dryRun = true;
    else if (argv[i] === '--path' && argv[i + 1]) {
      args.customPath = argv[++i];
    }
  }
  return args;
}

function copyDirSync(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirSync(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function rmDirSync(dirPath) {
  fs.rmSync(dirPath, { recursive: true, force: true });
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  // Resolve bundled skill source
  const pkgRoot = path.resolve(new URL(import.meta.url).pathname.replace(/^\/([A-Z]:)/, '$1'), '..', '..');
  const skillSrc = path.join(pkgRoot, 'skill', SKILL_NAME);

  if (!fs.existsSync(skillSrc)) {
    console.error(`Error: bundled skill not found at ${skillSrc}`);
    process.exit(1);
  }

  const skillMd = path.join(skillSrc, 'SKILL.md');
  if (!fs.existsSync(skillMd)) {
    console.error(`Error: SKILL.md missing from bundled skill at ${skillSrc}`);
    process.exit(1);
  }

  // Resolve destination
  const baseDir = args.customPath
    ? path.resolve(args.customPath)
    : path.join(os.homedir(), '.claude', 'skills');
  const dest = path.join(baseDir, SKILL_NAME);

  console.log(`\nSkill:       ${SKILL_NAME}`);
  console.log(`Source:      ${skillSrc}`);
  console.log(`Destination: ${dest}`);
  if (args.dryRun) console.log('Mode:        dry-run (no changes will be made)\n');
  else if (args.force) console.log('Mode:        force (existing destination will be replaced)\n');
  else console.log('');

  if (args.dryRun) {
    console.log('Dry-run complete. No files were written.');
    return;
  }

  // Check existing destination
  if (fs.existsSync(dest)) {
    if (!args.force) {
      console.error(`Error: ${dest} already exists.`);
      console.error(`Run with --force to overwrite:\n`);
      console.error(`  npx @rami/screenshot-to-design-kit --force`);
      process.exit(1);
    }
    console.log(`Removing existing destination...`);
    rmDirSync(dest);
  }

  // Create parent dir if needed
  fs.mkdirSync(baseDir, { recursive: true });

  // Copy skill
  console.log('Copying skill...');
  copyDirSync(skillSrc, dest);

  console.log(`\nInstalled successfully to:\n  ${dest}\n`);
  console.log('To use in Claude Code, add this to your project CLAUDE.md:\n');
  console.log(`  Use the skill at ~/.claude/skills/${SKILL_NAME}/SKILL.md\n`);
  console.log('Or reference it directly in a prompt:\n');
  console.log(`  "Using the screenshot-to-design-kit skill, convert my screenshots into a React/Tailwind design kit."\n`);
  console.log('Place your UI screenshots in:\n');
  console.log('  references/screenshots/\n');
}

main();
