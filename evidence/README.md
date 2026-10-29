# Final project evidence

These items must be captured from the real GitHub Actions run and the real
OpenShift learner cluster. They are intentionally not represented by mock
screenshots or invented output.

1. `cicd-github-validate`: after GitHub Actions passes, paste the job output
   showing checkout, Python setup, dependency installation, Flake8, and Nose.
2. `oc-pipelines-console-pvc-details.png`: capture the `pipeline-workspace`
   PVC details showing storage class `skills-network-learner` and capacity
   `1Gi`.
3. `oc-pipelines-oc-final.png`: capture the Tekton pipeline definition with
   `cleanup`, `git-clone`, `flake8`, `nose`, `buildah`, and `deploy`.
4. `oc-pipelines-oc-green.png`: capture a successful PipelineRun with all six
   tasks completed.
5. `oc-pipeline-application-logs`: paste the real application pod logs showing
   `SERVICERUNNING` and port `8000`.

Save both screenshots in this directory using the exact filenames above.
