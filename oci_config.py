compartment_id = "ocid1.compartment.oc1..xxxx"
auth_profile = "xxxx"
service_endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
embeddings_model_id = "cohere.embed-english-v3.0"
llm_model_id = "cohere.command" #meta.llama-2-70b-chat
llm_model_kwargs = {"temperature": 0, "top_p": 0.75, "max_tokens": 4096}
embeddings_model_kwargs = {"temperature": 0, "top_p": 0.75, "max_tokens": 512}