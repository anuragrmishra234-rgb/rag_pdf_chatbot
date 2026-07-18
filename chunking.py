text = """
Operating System is system software.

CPU Scheduling decides which process gets CPU.

Deadlock occurs when two or more processes wait forever.
"""

chunk_size = 5

chunks = []

for i in range(0, len(text), chunk_size):

    chunk = text[i:i + chunk_size]

    chunks.append(chunk)

print(chunks)