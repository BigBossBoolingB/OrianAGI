import unittest
import json
import os
from orianagi import OrianAGI, VariationalState, HamiltonianLandscape, Node

class TestOrianAGI(unittest.TestCase):
    def setUp(self):
        self.config_path = 'system_config.json'
        with open(self.config_path, 'r') as f:
            self.config_data = json.load(f)

    def test_from_json(self):
        model = OrianAGI.from_json(self.config_data)
        self.assertEqual(model.system_id, "QAATA-GENESIS-V1.2")
        self.assertEqual(model.architect, "Josephis K. Wade")
        self.assertEqual(model.variational_state.intent_vector, "|Ψ(θ)⟩")
        self.assertEqual(len(model.node_manager.nodes), 3)

    def test_status_report(self):
        model = OrianAGI.from_json(self.config_data)
        report = model.status_report()
        self.assertEqual(report['system_id'], "QAATA-GENESIS-V1.2")
        self.assertEqual(report['nodes_active'], 3)

    def test_node_manager(self):
        model = OrianAGI.from_json(self.config_data)
        node = model.node_manager.get_node("DEN-01")
        self.assertIsNotNone(node)
        self.assertEqual(node.name, "Denver Citadel")

        non_existent = model.node_manager.get_node("NON-EXISTENT")
        self.assertIsNone(non_existent)

    def test_train(self):
        model = OrianAGI.from_json(self.config_data)
        success = model.train("large_dataset_mock")
        self.assertTrue(success)

    def test_multimodal(self):
        model = OrianAGI.from_json(self.config_data)
        audio_res = model.multimodal.process_audio(None)
        self.assertEqual(audio_res['modality'], 'audio')
        video_res = model.multimodal.process_video(None)
        self.assertEqual(video_res['modality'], 'video')

    def test_world_model(self):
        model = OrianAGI.from_json(self.config_data)
        prediction = model.world_model.predict_next_state(None, None)
        self.assertEqual(prediction['predicted_state'], 'minimized_energy_state')

    def test_agent_team(self):
        model = OrianAGI.from_json(self.config_data)
        results = model.agent_team.coordinate_task("Solve quantum gravity")
        self.assertEqual(len(results), 3)
        self.assertIn("completed by Strategist", results[0])

    def test_quantum_competitive_features(self):
        model = OrianAGI.from_json(self.config_data)
        attn = model.quantum_entangled_attention(None, None, None)
        self.assertIn("Coherent", attn)
        genetics = model.genetic_sequence_alignment("ATGC")
        self.assertIn("Optimized", genetics)

if __name__ == '__main__':
    unittest.main()
