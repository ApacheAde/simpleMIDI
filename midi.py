from midiutil.MidiFile import MIDIFile

# Create a MIDIFile object
mf = MIDIFile(1)

# Add track names and tempo
mf.addTrackName(0, 0, "Example Track")
mf.addTempo(0, 0, 120)

# Set up the instrument (in this case, a piano)
channel = 0
instrument = 0
mf.addProgramChange(0, channel, 0, instrument)

# Add some notes
pitch = 60  # C4
time = 0
duration = 1
mf.addNote(0, channel, pitch, time, duration, 100)

pitch = 62  # D4
time = 1
duration = 1
mf.addNote(0, channel, pitch, time, duration, 100)

pitch = 64  # E4
time = 2
duration = 1
mf.addNote(0, channel, pitch, time, duration, 100)

# Save the MIDI file
with open("example.mid", "wb") as output_file:
  mf.writeFile(output_file)
