import random

def extract_configs(file_path):
    """
    Reads the file at `file_path` and extracts sections of text that
    fall between "BEGIN_CFG" and "END_CFG", inclusive.
    
    Returns:
        list of str: A list where each element is one configuration section.
    """
    with open(file_path, 'r') as file:
        content = file.read()
        
    configs = []
    # Split the content by "BEGIN_CFG"
    sections = content.split("BEGIN_CFG")
    
    for section in sections[1:]:  # Skip text before the first "BEGIN_CFG"
        end_idx = section.find("END_CFG")
        if end_idx != -1:
            # Extract the content between BEGIN_CFG and END_CFG (inclusive)
            config_content = section[:end_idx].strip()
            config_full = "BEGIN_CFG\n" + config_content + "\nEND_CFG"
            configs.append(config_full)
    
    return configs

def split_list_by_ratio(input_list, ratio=0.05):
    """
    Randomly splits `input_list` into two parts by `ratio`.
    
    The first part contains approximately `ratio * 100` percent of items,
    and the second part contains the rest.
    
    For example, ratio=0.05 results in:
        - 5% part (validate set)
        - 95% part (training set)
    
    Returns:
        tuple of (list, list): (larger_part, smaller_part)
    """
    # Number of elements for the smaller subset
    small_subset_len = int(len(input_list) * ratio)
    
    # Randomly sample for the small subset
    smaller_part = random.sample(input_list, small_subset_len)
    
    # The remaining items form the larger subset
    larger_part = [item for item in input_list if item not in smaller_part]
    
    return larger_part, smaller_part

def save_configs_to_file(configs_list, output_file):
    """
    Writes each configuration in `configs_list` to `output_file`,
    overwriting existing contents, and adds a blank line after each config.
    """
    with open(output_file, 'w') as file:
        for config in configs_list:
            file.write(config + '\n\n')

def append_configs_to_file(configs_list, output_file):
    """
    Appends each configuration in `configs_list` to `output_file`,
    adding a blank line after each config.
    """
    with open(output_file, 'a') as file:
        for config in configs_list:
            file.write(config + '\n\n')

def main():
    file_path = "converted.cfg"
    
    # 1. Extract configs
    configs_list = extract_configs(file_path)
    print("len(configs_list):", len(configs_list))
    
    # 2. Split into training (95%) and validation (5%) if >= 20 configs
    if len(configs_list) >= 20:
        added, validate = split_list_by_ratio(configs_list, ratio=0.05)
        print("95% part:", len(added))
        print("5% part:", len(validate))
    else:
        # If fewer than 20 configs, put everything in 'added'
        added = configs_list
        validate = []
    
    # 3. Save the validation set to "validate.cfg"
    validate_output_path = 'validate.cfg'
    save_configs_to_file(validate, validate_output_path)
    print(f"Configurations saved to {validate_output_path}")
    
    # 4. Append training set to "train.cfg"
    append_configs_to_file(added, "train.cfg")
    print("Configurations appended to train.cfg")

if __name__ == "__main__":
    main()
