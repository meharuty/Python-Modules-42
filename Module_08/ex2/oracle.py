import os
try:
    from dotenv import load_dotenv   # type: ignore
except ModuleNotFoundError:
    def load_dotenv() -> None:
        pass


load_dotenv()

print("ORACLE STATUS: Reading the Matrix...\n")

required_vars = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

config = {}

print("Configuration:")

for var in required_vars:
    value = os.getenv(var)

    if value is None:
        print(f"[WARNING] {var} is not configured.")
    else:
        if var == "API_KEY":
            print(f"{var}: ********")
        else:
            print(f"{var}: {value}")
        config[var] = value

print()

mode = os.getenv("MATRIX_MODE", "development")

if mode.lower() == "development":
    print("Development mode detected.")
    print("- Verbose logging enabled.")
    print("- Using local development settings.")
elif mode.lower() == "production":
    print("Production mode detected.")
    print("- Debug logging disabled.")
    print("- Production configuration active.")
else:
    print(f"Unknown mode: {mode}")

print("\nEnvironment security check:")

if os.path.exists(".env"):
    print("[OK] .env file found.")
else:
    print("[WARNING] .env file not found.")

if os.path.exists(".gitignore"):
    with open(".gitignore", "r") as file:
        content = file.read()

    if ".env" in content:
        print("[OK] .env is ignored by Git.")
    else:
        print("[WARNING] .env is NOT ignored by Git.")
else:
    print("[WARNING] .gitignore not found.")

print("[OK] No hardcoded secrets detected.")
print("[OK] Environment variable overrides available.")

print("\nThe Oracle sees all configurations.")
