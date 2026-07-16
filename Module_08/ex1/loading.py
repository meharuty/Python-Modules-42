import sys
import importlib
from typing import Any
import importlib.util


print("LOADING STATUS: Loading programs...")
print("Checking dependencies...")

PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
    "requests": "Network access (optional)"
}


def check_dependencies() -> tuple[dict[str, Any], list[str]]:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")

    available = {}
    missing = []

    for package, description in PACKAGES.items():
        spec = importlib.util.find_spec(package)

        if spec is None:
            print(f"[MISSING] {package}")
            missing.append(package)
        else:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "Unknown")
            print(f"[OK] {package} ({version}) - {description}")
            available[package] = module

    return available, missing


def show_installation_help() -> None:
    print("\nSome required packages are missing.\n")

    print("Install using pip:")
    print("    pip install -r requirements.txt\n")

    print("Or install using Poetry:")
    print("    poetry install\n")

    print("Run again after installing the dependencies.")


def compare_dependency_managers() -> None:
    print("\nDependency management")
    print("---------------------")
    print("pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print()


def analyze_matrix_data(np: Any, pd: Any, plt: Any) -> None:
    print("\nAnalyzing Matrix data...")

    data = np.random.randint(0, 100, size=1000)

    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame({"Signal": data})

    print("\nStatistics")
    print(df.describe())

    print("\nGenerating visualization...")

    plt.figure(figsize=(8, 5))
    plt.hist(df["Signal"], bins=20)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal")
    plt.ylabel("Frequency")

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()

    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    available, missing = check_dependencies()

    required = ["numpy", "pandas", "matplotlib"]

    if any(pkg in missing for pkg in required):
        show_installation_help()
        sys.exit(1)

    compare_dependency_managers()

    analyze_matrix_data(
        available["numpy"],
        available["pandas"],
        available["matplotlib"].pyplot,
    )


if __name__ == "__main__":
    main()
