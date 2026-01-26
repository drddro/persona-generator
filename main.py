import json

from controler.persona_controler import PersonaControler

def main():
    with open("resources/config.json", "r") as config_file:
        config = json.load(config_file)
        config_file.close()

    persona_controller = PersonaControler(config)

    persona_controller.generate_persona_from_scheme(
        path_to_persona="resources/inputs/input.txt"
    )

if __name__ == "__main__":
    main()