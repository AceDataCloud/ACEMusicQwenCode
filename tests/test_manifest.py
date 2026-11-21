import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PluginContract(unittest.TestCase):
    def test_service_and_credential_binding(self):
        manifest = json.loads((ROOT / "qwen-extension.json").read_text())
        server = manifest["mcpServers"]["acemusic"]
        self.assertEqual(server["headers"], {"Authorization": "Bearer $ACEDATACLOUD_ACEMUSIC_TOKEN"})
        self.assertTrue((ROOT / manifest["contextFileName"]).is_file())
        self.assertEqual(server['httpUrl'], "https://acemusic.mcp.acedata.cloud/mcp")

        names = server['includeTools']
        self.assertEqual(set(names), {"acemusic_" + name for name in (
            "list_models", "get_capabilities", "generate_music", "generate_custom_music",
            "generate_lyrics", "upload_audio", "cover_audio", "mashup_audio", "get_task",
            "get_tasks_batch", "list_tasks",
        )})
