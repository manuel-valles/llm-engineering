# Day 3: Agentic AI Models

*Agentic AI* is a group of systems that act with autonomy to achieve a goal. They plan, decide next steps, use tools, observe results, adjust,
and repeat. Basically, it breaks a goal into tasks, calls APIs, runs code, searches the web, maintains state over time and self-corrects!! 

Some examples are AutoGPT, CrewAI, and coding agents in Cursor that refactor across files.

## Claude Code

First time using [Claude AI](https://claude.ai/new) in general? Give it a go and pick the free tier :) This onboarding even gives you the [Claude Code](https://claude.com/product/claude-code) installation process.
Work with Claude directly in your codebase. Build, debug, and ship from your terminal, IDE, Slack, or the web. Describe what you need, and Claude handles the rest.

- From PowerShell run: `$ irm https://claude.ai/install.ps1 | iex` 

> NOTE: Claude Code is NOT FREE!! But this is the trick, you can use Ollama locally with a local or a cloud free model!! https://ollama.com/blog/claude

- Run (this will stay until you kill the terminal): 
    ```sh
    export ANTHROPIC_AUTH_TOKEN=ollama
    export ANTHROPIC_BASE_URL=http://localhost:11434
    ```

> IMPORTANT: Keep in mind that you have been already logged in, so to be able to do the workaround you need to log out inside Claude Code

- Logout: 
    - `$ claude` 
    - Inside the Claude terminal `> /logout`

- Run Claude with a local model: `$ claude --model qwen2.5-coder:3b`

> NOTE: Since the cloud qwen3-code is also paid, we had to go for a previous version and a 3b model. Either way, it is too slow! It's better to use the integrated Agents in Cursor.