import gpt_2_simple as gpt2

outdated_file_path = "outdated_user_guide.txt"
reference_file_path = "new_material.txt"

# Read files
with open(outdated_file_path, 'r') as file:
    outdated_text = file.read()
with open(reference_file_path, 'r') as file:
    reference_text = file.read()

# Concatenate the outdated user guide with the new reference material
input_prompt = outdated_text + "\n\n" + reference_text

# Start a TensorFlow session
sess = gpt2.start_tf_sess()

# Load the GPT2 model
gpt2.load_gpt2(sess, model_name="124M")

# Generate text based on the prompt
generated_text = gpt2.generate(sess, prefix=input_prompt, length=200)[0]

print("Generated text:")
print(generated_text)
