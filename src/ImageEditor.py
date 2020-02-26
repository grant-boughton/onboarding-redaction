import json
import boto3
from PIL import Image, ImageDraw


def lambdaHandler(event, context):
    s3 = boto3.resource("s3")
    boxes = json.loads(event["data"])
    key = event["key"]
    bucket = event["bucket"]
    redactImageS3(boxes, key, bucket, s3)


# Redacts image found in S3 bucket
def redactImageS3(boxes, key, bucket, s3):
    if "/" in key:
        # remove uploading user from key
        splitKey = key.split("/")
        fileName = splitKey[len(splitKey) - 1]
    else:
        fileName = key

    try:
        localFileName = '/tmp/' + fileName
        s3.Bucket(bucket).download_file(key, localFileName)
    except:
        raise

    redactImage(boxes, localFileName, "/tmp/edited.jpg")



    s3.upload_file("/tmp/edited.jpg", bucket, "redacted/" + fileName)
    return bucket + ".s3.amazonaws.com/redacted/" + fileName


# Redacts image stored locally
def redactImage(boxes, inFile, outFile):
    try:
        image = Image.open(inFile)
        drawing = ImageDraw.Draw(image)
        width, height = image.size
    except:
        raise

    for box in boxes:
        # box edges are a ratio of the width and height
        X1 = box["left"] * width
        Y1 = box["bottom"] * height


        X2 = box["right"] * width
        Y2 = box["top"] * height

        drawing.rectangle([(X1, Y1), (X2, Y2)], "black", "black")

    image.save(outFile, "PNG")