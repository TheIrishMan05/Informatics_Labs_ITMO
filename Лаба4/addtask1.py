import ruamel.yaml
import json
yaml = ruamel.yaml.YAML(typ='safe')
with open('Вторник.yml', encoding="utf-8") as f_in:
    data = yaml.load(f_in)
with open('Вторник(итог)(для тестов).json', 'w', encoding="utf-8") as f_out:
    json.dump(data, f_out, indent=2, ensure_ascii=False)

