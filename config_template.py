# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root

# ============================================================================
# CONFIG_TEMPLATE.PY - SYSTEM CONFIGURATION TEMPLATE (Gemini Only)
# ============================================================================

# This template provides the structure for config.py including Gemini API keys, model
# selections, file paths, and operational parameters.

# KEY RESPONSIBILITIES:
# - Gemini API key and authentication management template
# - Gemini model configuration for different use cases
# - File system path configuration
# - System operational parameters
# - Environment-specific settings

# SECURITY CONSIDERATIONS:
# - API keys should be moved to environment variables in production
# - Sensitive configuration should not be committed to version control
# - Copy this template to config.py and add your actual Gemini API key

# ARCHITECTURAL INTEGRATION:
# - Used by all modules requiring AI model access
# - Provides centralized Gemini model selection strategy
# - Enables easy switching between different Gemini configurations

# ============================================================================
# Gemini API key (move to environment variable in production!)
GEMINI_API_KEY = "your_gemini_api_key_here"

# Gemini model selection: "gemini-2.5-flash" (default), "gemini-pro", etc.
GEMINI_MODEL = "gemini-2.5-flash"

# --- Module folder structure ---
MODULES_DIR = "modules"
DEFAULT_MODULE = "The_Thornwood_Watch"

# --- Web Interface Configuration ---
WEB_PORT = 8357                                         # Port for the web interface

# --- END OF FILE config_template.py ---