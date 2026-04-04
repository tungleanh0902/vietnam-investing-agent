# Vietnam Investing Agent

This repository contains skills and MCP servers for analyzing the Vietnamese stock market.

## Structure

- `.claude-plugin/`: Plugin manifest for Claude Code / other compatible agent platforms.
- `skills/`: Agent instructions (.md files) defining execution workflows (e.g., fundamental analysis).
- `mcp-servers/`: Model Context Protocol servers to provide data execution capabilities (e.g., `vnstock-mcp`).

## Usage

Agents launched in this folder will automatically read the `.claude-plugin/marketplace.json` to load the `fundamental-analyst` skill. 

Make sure your environment variables (like `DNSE_API_KEY`, etc. if you use `vnstock-mcp`) are set in a `.env` file at the root of this project.
