🦁 LEO - AI-Powered Command Line Assistant 🚀

📝 Overview

LEO is an intelligent command-line assistant that transforms natural language prompts into accurate system commands using a cloud-based Large Language Model (LLM).

Designed for developers, sysadmins, and power users, LEO automates command execution, ensures security, and provides transparent logging, making it an ideal assistant for system administration, cloud operations, and development workflows.

⚡ Key Features

✅ AI-Powered Command Generation – Converts natural language prompts into shell commands.
🔍 Context-Aware Execution – Detects missing details and asks clarifying questions.
🔑 Secure Secrets Management – Locally stores sensitive data and injects it securely.
🤖 Autonomous & User-Controlled Modes – Supports automatic or manual execution approval.
🛡️ Built-in Safety & Validation – Ensures commands are safe before execution.
⚙️ Error Detection & Recovery – Logs output, detects errors, and retries when necessary.
📜 Logging & Feedback System – Provides execution logs and transparent feedback.

🏗️ Architecture Overview

LEO follows a modular and structured execution pipeline for safety, accuracy, and flexibility:

1️⃣ Command Line Interface – Captures user input.
2️⃣ Safety & Context Analysis – Ensures prompt security and completeness.
3️⃣ Interactive Questioning Module – Collects missing details from the user.
4️⃣ Secrets Manager – Securely stores and injects credentials/API keys.
5️⃣ Cloud LLM Service – Generates accurate shell commands.
6️⃣ Command Generation Module – Formats and validates commands.
7️⃣ Command Execution Center – Runs commands and collects output.
8️⃣ Command Output Verification – Detects errors and verifies success.
9️⃣ Assertion Commands Module – Runs additional checks to ensure correctness.
🔟 Logging & Feedback Module – Logs execution details and provides insights.

📌 Architecture Diagram Available in the repository for visual understanding.

🛣️ Roadmap

🔹 Phase 1: Core Development
✔️ Implement CLI input handling
✔️ Integrate LLM for command generation
✔️ Add safety validation and context analysis
✔️ Implement secrets management

🔹 Phase 2: Execution & Verification
✔️ Develop command execution and output collection
✔️ Add error detection and automated recovery
✔️ Implement assertion-based verification

🔹 Phase 3: UX & Enhancements
🔜 Improve interactive questioning for missing details
🔜 Enhance user control over execution modes
🔜 Optimize logging and feedback visualization

🔹 Phase 4: Advanced Features
🔜 Support for multi-step automation workflows
🔜 Integration with external API services
🔜 Plugin support for additional command sets

📅 Ongoing: Bug fixes, security improvements, and community feedback incorporation.

🚀 Getting Started

📥 Installation

git clone https://github.com/your-repo/leo.git
cd leo
pip install -r requirements.txt

⚡ Usage Example

leo "Create a new Docker container and start a web server"

👀 Watch it in action! LEO will analyze, validate, and execute the necessary commands.

🤝 Contributing

🔗 We welcome contributions! Feel free to submit issues, feature requests, or pull requests to enhance LEO.

📌 License

📝 This project is open-source under the MIT License.

🚀 Power up your command-line experience with LEO – your AI-driven assistant! 🚀
