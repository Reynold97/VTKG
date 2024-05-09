# Voice to Knowledge Graph Demo

## Project Description
This demo showcases a Gradio application that converts spoken audio into a visual knowledge graph. Users can record their voice, and the application transcribes the audio, extracts relevant nodes and relationships, and visualizes them in a Neo4j knowledge graph.

## System Requirements
- Anaconda or Miniconda

## Installation

### Step 1: Clone the Repository
Clone this repository to your local machine using:
```bash
git clone [URL_OF_YOUR_REPO]
cd [REPO_NAME]
```

### Step 2: Create a Conda Environment
Create a Conda environment using:
```bash
conda create -p ./env python=3.10 -y
```

### Step 3: Activate the Environment
Activate the newly created environment:
```bash
conda activate ./env
```

### Step 4: Install Required Packages
Install all required packages listed in requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 5: Create a Neo4j database instance
You will need to have a running Neo4j instance. One option is to create a [free Neo4j database instance in their Aura cloud service](https://neo4j.com/cloud/platform/aura-graph-database/). You can also run the database locally using the [Neo4j Desktop application](https://neo4j.com/download/), or running a docker container. You can run a local docker container by running the executing the following script:
```
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -d \
    -e NEO4J_AUTH=neo4j/pleaseletmein \
    -e NEO4J_PLUGINS=\[\"apoc\"\]  \
    neo4j:latest
```    
If you are using the docker container, you need to wait a couple of second for the database to start.

### Step 6: Create a .env file 
Create a .env file in the root directory with the following structure 
```bash
DEEPGRAM_API_KEY=
OPENAI_API_KEY=
NEO4J_USER=
NEO4J_PASS=
NEO4J_URL=
```

### Step 7: Running the Application
Run the application with:
```bash
python app.py
```
This will start the Gradio app, which is accessible via a web browser. Follow the on-screen instructions to record your voice and generate the knowledge graph.

### Usage
Record Audio: Click the 'Record' button and speak into your microphone.
Submit: Submit the audio recording to process.
View Graph: After processing, go to your Neo4j instance to inspect the knowledge graph.