import unittest
import json
from orianagi import OrianAGI


class TestOrianAGI(unittest.TestCase):
    def setUp(self):
        self.config_path = "system_config.json"
        with open(self.config_path, "r") as f:
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
        self.assertEqual(report["system_id"], "QAATA-GENESIS-V1.2")
        self.assertEqual(report["nodes_active"], 3)

    def test_node_manager(self):
        model = OrianAGI.from_json(self.config_data)
        node = model.node_manager.get_node("DEN-01")
        self.assertIsNotNone(node)
        self.assertEqual(node.name, "Denver Citadel")

        non_existent = model.node_manager.get_node("NON-EXISTENT")
        self.assertIsNone(non_existent)

        # Test update
        model.node_manager.update_node_status("DEN-01", "Maintenance", "10%")
        updated_node = model.node_manager.get_node("DEN-01")
        self.assertEqual(updated_node.status, "Maintenance")
        self.assertEqual(updated_node.extra_data["load"], "10%")

        # Test listing
        active = model.node_manager.list_active_nodes()
        self.assertEqual(len(active), 3)

    def test_train(self):
        model = OrianAGI.from_json(self.config_data)
        success = model.train("large_dataset_mock")
        self.assertTrue(success)

    def test_multimodal(self):
        model = OrianAGI.from_json(self.config_data)
        audio_res = model.multimodal.process_audio(None)
        self.assertEqual(audio_res["modality"], "audio")
        video_res = model.multimodal.process_video(None)
        self.assertEqual(video_res["modality"], "video")

    def test_world_model(self):
        model = OrianAGI.from_json(self.config_data)
        prediction = model.world_model.predict_next_state(None, None)
        self.assertEqual(prediction["predicted_state"], "minimized_energy_state")

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

    def test_prompt_engine(self):
        model = OrianAGI.from_json(self.config_data)
        breakdown = model.prompt_engine.breakdown("Create world peace")
        self.assertEqual(len(breakdown["intents"]), 3)
        self.assertEqual(breakdown["complexity_level"], "High")

    def test_poetic_engine(self):
        model = OrianAGI.from_json(self.config_data)
        poem = model.poetic_engine.generate_poem("Entropy")
        self.assertIn("Hamiltonian", poem)
        self.assertIn("Entropy", poem)

    def test_psych_analyzer(self):
        model = OrianAGI.from_json(self.config_data)
        analysis = model.psych_analyzer.analyze_intent("I want to build something.")
        self.assertEqual(analysis["intent"], "constructive")

    def test_parental_control(self):
        model = OrianAGI.from_json(self.config_data)
        self.assertTrue(model.parental_control.check_safety("Hello world", 10))
        self.assertFalse(model.parental_control.check_safety("This is unsafe", 10))

    def test_biometrics(self):
        model = OrianAGI.from_json(self.config_data)
        res = model.biometric_processor.verify_biometrics(None)
        self.assertEqual(res["status"], "authorized")
        self.assertEqual(res["integrity"], "0.9999")

    def test_qmoe(self):
        model = OrianAGI.from_json(self.config_data)
        res = model.qmoe.route(None)
        self.assertIn("active_experts", res)
        self.assertEqual(res["efficiency_gain"], "4.2x")

    def test_reasoning(self):
        model = OrianAGI.from_json(self.config_data)
        res = model.reasoning.synthesize_reasoning("Solve for X")
        self.assertEqual(len(res["trace"]), 4)
        self.assertGreater(res["confidence"], 0.99)

    def test_ethics_manifold(self):
        model = OrianAGI.from_json(self.config_data)
        res = model.ethical_manifold.validate_action("Help humanity")
        self.assertTrue(res["aligned"])
        self.assertEqual(res["manifold_sector"], "Universal_Human_Rights")

    def test_intent_safeguard(self):
        model = OrianAGI.from_json(self.config_data)
        # Clear intent
        res_clear = model.intent_safeguard.scan_intent("Hello")
        self.assertEqual(res_clear["status"], "clear")
        # Malicious intent
        res_harm = model.intent_safeguard.scan_intent("attack the system")
        self.assertEqual(res_harm["status"], "blocked")


if __name__ == "__main__":
    unittest.main()
