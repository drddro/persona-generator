import json

class JsonService:

    def __init__(self, config):       
        
        self.output_path = config["output"]["output_path"]
        self.output_filename = config["output"]["output_filename"]

        self.path_to_scheme = config["persona_scheme_path"]

    def get_scheme(self) -> dict:
        try:
            with open(self.path_to_scheme, 'r') as file:
                json_data = json.load(file)
                return remove_json_values(json_data)
        except Exception as e:
            raise e
        
    def write_persona_to_json(self, persona_json_str: str) -> None:
        with open(f"{self.output_path}/{self.output_filename}", 'w') as json_file:
            loaded_json_str = json.loads(persona_json_str)
            json.dump(loaded_json_str, json_file, indent=4)
            json_file.close()
        

#recursive function to remove all values from a json dict, keeping only the keys
def remove_json_values(json_data: dict) -> dict:
    for key in json_data.keys():
        if isinstance(json_data[key], dict):
            json_data[key] = remove_json_values(json_data[key])
        elif key == "projectHistory":
            json_data[key] = remove_json_values(json_data[key][0])
        else:
            json_data[key] = None
    return json_data