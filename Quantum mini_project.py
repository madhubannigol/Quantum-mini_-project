from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create the quantum circuit for a single player's turn
def create_player_turn_circuit():
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit
# Simulate a single player's turn
def simulate_player_turn():
    circuit = create_player_turn_circuit()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    return list(counts.keys())[0]
# Main game loop
def play_ludo_game():
    num_players = 4
    player_positions = [0] * num_players

    while True:
        for player in range(num_players):
            print(f"Player {player+1}, it's your turn!")
            dice_roll = simulate_player_turn()
            dice_value = int(dice_roll, 2) + 1
            print(f"You rolled a {dice_value}!")
            player_positions[player] += dice_value
            print(f"Your position: {player_positions[player]}")    
         
            # Check for winning condition
            if player_positions[player] >= 100:
                print(f"Player {player+1} wins!")
                return

# Start the game
play_ludo_game()