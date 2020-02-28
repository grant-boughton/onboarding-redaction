# onboarding-redaction
Lambda to redact image

## Important Note
This python script requires Pillow to be installed. If deploying to an AWS Lambda, Pillow (and any other dependencies) must be installed using a Linux machine. If you are not using a Linux OS this can be done by running a Linux Docker image with a volume mounted to your local machine, then run `pip install --target {path/to/mounted/volume} Pillow`
