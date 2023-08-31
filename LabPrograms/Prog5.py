import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    # Create initial heap of Huffman nodes
    heap = []
    for i in range(len(characters)):
        node = HuffmanNode(characters[i], frequencies[i])
        heapq.heappush(heap, node)

    # Build Huffman tree by combining nodes until there is only one node left in the heap
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)

        # Create a new node with combined frequency and left/right children
        combined_freq = left_node.freq + right_node.freq
        combined_node = HuffmanNode(None, combined_freq)
        combined_node.left = left_node
        combined_node.right = right_node

        heapq.heappush(heap, combined_node)

    return heapq.heappop(heap)

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    # Leaf node represents a character
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    # Traverse left branch (0) and append '0' to the current code
    build_huffman_codes(root.left, current_code + '0', huffman_codes)

    # Traverse right branch (1) and append '1' to the current code
    build_huffman_codes(root.right, current_code + '1', huffman_codes)

def encode_string(string, huffman_codes):
    encoded_string = ''
    for char in string:
        encoded_string += huffman_codes[char]
    return encoded_string

def decode_string(encoded_string, root):
    decoded_string = ''
    current_node = root
    for bit in encoded_string:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # Leaf node represents a character
        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = root

    return decoded_string

# Get inputs from the user
n = int(input("Enter the number of characters: "))
characters = []
frequencies = []
for i in range(n):
    char = input("Enter character: ")
    frequency = float(input("Enter probability: "))
    characters.append(char)
    frequencies.append(frequency)

# Build Huffman tree
huffman_tree = build_huffman_tree(characters, frequencies)

# Build Huffman codes
huffman_codes = {}
build_huffman_codes(huffman_tree, '', huffman_codes)

# Encode and decode strings
string = input("Enter a string to encode: ")
encoded_string = encode_string(string, huffman_codes)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(char, ":", code)

print("Encoded string:", encoded_string)

# Decode a Huffman-encoded string
decode_choice = input("Do you want to decode the encoded string? (Y/N): ")
if decode_choice.lower() == 'y':
    decoded_string = decode_string(encoded_string, huffman_tree)
    print("Decoded string:", decoded_string)

# Decode a binary number entered by the user
decode_new_choice = input("Do you want to decode a new binary number? (Y/N): ")
if decode_new_choice.lower() == 'y':
    binary_number = input("Enter the binary number to decode: ")
    decoded_new_string = decode_string(binary_number, huffman_tree)
    print("Decoded string:", decoded_new_string)
