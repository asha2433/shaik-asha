FROM python:3.8-slim
#RUN pip install pyats
RUN pip install pyats[full]
RUN apt-get update && apt-get install -y openssh-client
# Set the working directory in the container
WORKDIR /testwork




# Copy the Python script to the container
COPY show_version.py /testwork/
COPY my_yaml1.yaml /testwork/


# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/show_version.py"]
