from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

BENCHMARK_API_KEY = os.environ.get("BENCHMARK_API_KEY")


@app.route("/trigger-benchmark", methods=["POST"])
def trigger_benchmark():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {BENCHMARK_API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    branch = data.get("branch")
    args = data.get("args")
    issue_number = data.get("issue_number")

    if not branch:
        return jsonify({"error": "Missing branch"}), 400
    if not args:
        return jsonify({"error": "Missing args"}), 400
    if not issue_number:
        return jsonify({"error": "Missing issue_number"}), 400

    # TODO: trigger experiment
    print(f"Triggering benchmark for issue #{issue_number}")
    print(f"Branch: {branch}")
    print(f"Arguments: {args}")

    # Example of running a script in the background:
    # command = ["/path/to/your/benchmark_script.sh", branch, args, str(issue_number)]
    # subprocess.Popen(command)

    return jsonify({"message": "Benchmark triggered successfully"}), 202


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
