{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "56f42e07-e87b-4736-96e1-469d2038919f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Importing standard Qiskit libraries\n",
    "from qiskit import QuantumCircuit, transpile\n",
    "from qiskit.tools.jupyter import *\n",
    "from qiskit.visualization import *\n",
    "from ibm_quantum_widgets import *\n",
    "from qiskit_aer import AerSimulator\n",
    "\n",
    "# qiskit-ibmq-provider has been deprecated.\n",
    "# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.\n",
    "from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session, Options\n",
    "\n",
    "# Loading your IBM Quantum account(s)\n",
    "service = QiskitRuntimeService(channel=\"ibm_quantum\")\n",
    "\n",
    "# Invoke a primitive inside a session. For more details see https://qiskit.org/documentation/partners/qiskit_ibm_runtime/tutorials.html\n",
    "# with Session(backend=service.backend(\"ibmq_qasm_simulator\")):\n",
    "#     result = Sampler().run(circuits).result()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cfa9ac22-4f0c-425a-b487-bb9486272660",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 4\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 4\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 1\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 1\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 5\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 8\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 5\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 2\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 6\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 12\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 9\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 3\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 7\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 16\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 10\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 4\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 8\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 17\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 11\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 8\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 9\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 21\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 12\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 12\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 10\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 22\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 13\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 16\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 11\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 26\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 17\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 17\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 15\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 27\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 21\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 21\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 16\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 28\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 22\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 25\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 20\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 32\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 23\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 29\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 24\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 33\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 27\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 33\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 28\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 37\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 28\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 37\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 32\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 38\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 29\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 41\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 36\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 42\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 30\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 42\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 40\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 46\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 34\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 46\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 41\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 50\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 38\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 47\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 42\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 54\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 39\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 48\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 43\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 55\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 43\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 49\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 47\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 56\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 44\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 53\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 51\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 57\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 48\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 57\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 52\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 58\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 49\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 61\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 56\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 62\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 50\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 65\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 60\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 66\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 51\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 69\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 61\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 67\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 52\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 73\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 65\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 71\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 56\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 77\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 66\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 72\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 57\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 78\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 70\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 76\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 61\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 82\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 71\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 77\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 65\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 83\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 75\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 78\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 69\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 84\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 79\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 79\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 73\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 85\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 80\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 80\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 77\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 89\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 81\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 81\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 81\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 93\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 82\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 85\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 85\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 94\n",
      "Player 1, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 83\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 86\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 86\n",
      "Player 4, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 95\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 87\n",
      "Player 2, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 90\n",
      "Player 3, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 90\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 99\n",
      "Player 1, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 91\n",
      "Player 2, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 91\n",
      "Player 3, it's your turn!\n",
      "You rolled a 1!\n",
      "Your position: 91\n",
      "Player 4, it's your turn!\n",
      "You rolled a 4!\n",
      "Your position: 103\n",
      "Player 4 wins!\n"
     ]
    }
   ],
   "source": [
    "from qiskit import QuantumCircuit, execute, Aer\n",
    "from qiskit.visualization import plot_bloch_multivector, plot_histogram\n",
    "\n",
    "# Create the quantum circuit for a single player's turn\n",
    "def create_player_turn_circuit():\n",
    "    circuit = QuantumCircuit(2, 2)\n",
    "    circuit.h(0)\n",
    "    circuit.cx(0, 1)\n",
    "    circuit.measure([0, 1], [0, 1])\n",
    "    return circuit\n",
    "# Simulate a single player's turn\n",
    "def simulate_player_turn():\n",
    "    circuit = create_player_turn_circuit()\n",
    "    backend = Aer.get_backend('qasm_simulator')\n",
    "    job = execute(circuit, backend, shots=1)\n",
    "    result = job.result()\n",
    "    counts = result.get_counts()\n",
    "    return list(counts.keys())[0]\n",
    "    # Main game loop\n",
    "def play_ludo_game():\n",
    "    num_players = 4\n",
    "    player_positions = [0] * num_players\n",
    "    \n",
    "    while True:\n",
    "        for player in range(num_players):\n",
    "            print(f\"Player {player+1}, it's your turn!\")\n",
    "            dice_roll = simulate_player_turn()\n",
    "            dice_value = int(dice_roll, 2) + 1\n",
    "            print(f\"You rolled a {dice_value}!\")\n",
    "            player_positions[player] += dice_value\n",
    "            print(f\"Your position: {player_positions[player]}\")\n",
    "            # Check for winning condition\n",
    "            if player_positions[player] >= 100:\n",
    "                print(f\"Player {player+1} wins!\")\n",
    "                return\n",
    "\n",
    "# Start the game\n",
    "play_ludo_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7ca80a0-5188-426f-95c7-21248287f6f1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {
     "0a1dbecab7eb4cbc8c5f93dd0b9c9a16": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_3c3aa17ac0324c229991fca16aab175f",
       "style": "IPY_MODEL_a1456c320e7f4508b44e619e9f29ceea",
       "value": "<h5>Status</h5>"
      }
     },
     "181f20faf6804b909b4ad37ff868c881": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "grid_template_areas": "\n                                       \". . . . right \"\n                                        ",
       "grid_template_columns": "20% 20% 20% 20% 20%",
       "width": "100%"
      }
     },
     "3c3aa17ac0324c229991fca16aab175f": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "95px"
      }
     },
     "3d7ad549c8424e2fbd4a1b309a24141e": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "145px"
      }
     },
     "44454297b7f342e4a948419b7680d977": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "4baa0fffa7aa49f0a733316bcd3d1390": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HBoxModel",
      "state": {
       "children": [
        "IPY_MODEL_76b2548b29cc413caf100c3c78149d2d",
        "IPY_MODEL_4dee9892eb824df4bc58661ad50ba418",
        "IPY_MODEL_0a1dbecab7eb4cbc8c5f93dd0b9c9a16",
        "IPY_MODEL_a79f2609a3914c91b15615bd95b23ba3",
        "IPY_MODEL_9521c155c37f4054a9d3dc859bb8fefc"
       ],
       "layout": "IPY_MODEL_9015afd5dae9429aaed4823a363d06d6"
      }
     },
     "4dee9892eb824df4bc58661ad50ba418": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_3d7ad549c8424e2fbd4a1b309a24141e",
       "style": "IPY_MODEL_f66d69b23a514a66b7ee4f587d51e6c4",
       "value": "<h5>Backend</h5>"
      }
     },
     "5568dafcfffc4893b5eacb6b8b54cc00": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "ButtonModel",
      "state": {
       "button_style": "primary",
       "description": "Clear",
       "layout": "IPY_MODEL_ce7ef379c7534558a22b987f28fc31c8",
       "style": "IPY_MODEL_a0eba4b9c877423baf7a6a4392746469",
       "tooltip": null
      }
     },
     "76b2548b29cc413caf100c3c78149d2d": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_fe4c6c42ca274941adc2f2e8a9ec89cd",
       "style": "IPY_MODEL_7b3db0be01e241dbb1d35ab482edfc23",
       "value": "<h5>Job ID</h5>"
      }
     },
     "7b3db0be01e241dbb1d35ab482edfc23": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "8993acee219447e6b29c52d312cee2a1": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "margin": "0px 0px 10px 0px"
      }
     },
     "9015afd5dae9429aaed4823a363d06d6": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "margin": "0px 0px 0px 37px",
       "width": "600px"
      }
     },
     "9521c155c37f4054a9d3dc859bb8fefc": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_44454297b7f342e4a948419b7680d977",
       "style": "IPY_MODEL_afb880c4152d41aaa08277edb316b881",
       "value": "<h5>Message</h5>"
      }
     },
     "a022234cd42b4e328e36ccadf9e8afaf": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_8993acee219447e6b29c52d312cee2a1",
       "style": "IPY_MODEL_c5e5046fa0e44ee69d7a51282b322915",
       "value": "<p style='font-family: IBM Plex Sans, Arial, Helvetica, sans-serif; font-size: 20px; font-weight: medium;'>Circuit Properties</p>"
      }
     },
     "a0eba4b9c877423baf7a6a4392746469": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "ButtonStyleModel",
      "state": {
       "font_family": null,
       "font_size": null,
       "font_style": null,
       "font_variant": null,
       "font_weight": null,
       "text_color": null,
       "text_decoration": null
      }
     },
     "a1456c320e7f4508b44e619e9f29ceea": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "a79f2609a3914c91b15615bd95b23ba3": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_d0a40ae8aa074f5fb0ed3c372bbc498d",
       "style": "IPY_MODEL_afc197617dd540e29057f48691c21026",
       "value": "<h5>Queue</h5>"
      }
     },
     "afb880c4152d41aaa08277edb316b881": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "afc197617dd540e29057f48691c21026": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "c5e5046fa0e44ee69d7a51282b322915": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "ce7ef379c7534558a22b987f28fc31c8": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "grid_area": "right",
       "padding": "0px 0px 0px 0px",
       "width": "70px"
      }
     },
     "d0a40ae8aa074f5fb0ed3c372bbc498d": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "70px"
      }
     },
     "ddca92249c2d494bb641440c4d656b2d": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "GridBoxModel",
      "state": {
       "children": [
        "IPY_MODEL_5568dafcfffc4893b5eacb6b8b54cc00"
       ],
       "layout": "IPY_MODEL_181f20faf6804b909b4ad37ff868c881"
      }
     },
     "f66d69b23a514a66b7ee4f587d51e6c4": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "2.0.0",
      "model_name": "HTMLStyleModel",
      "state": {
       "description_width": "",
       "font_size": null,
       "text_color": null
      }
     },
     "fe4c6c42ca274941adc2f2e8a9ec89cd": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "2.0.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "190px"
      }
     }
    },
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}