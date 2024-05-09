import gradio as gr

from tts import transcribe_audio
from kg import add_to_kg

def pipeline(audio_path):
    """Pipeline to comunicate tts and kg modules"""
    transcription = transcribe_audio(audio_path)
    graph_documents = add_to_kg(str(transcription))
    return f"Transcription: {transcription} \nNodes: {graph_documents[0].nodes} \nRelationships: {graph_documents[0].relationships}"


iface = gr.Interface(
    fn=pipeline,
    inputs=gr.Audio(sources="microphone", type="filepath", format="wav"),
    outputs="text",
    title="Voice to Knowledge Graph",
    description="Record an audio clip, get it transcribed using Deepgram, make nodes and relationships with an LLM, add them to a Neo4J KG."
)

if __name__ == "__main__":
    iface.launch()
