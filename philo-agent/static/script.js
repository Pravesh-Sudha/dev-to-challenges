let mediaRecorder;
let audioChunks = [];
let isRecording = false;

function toggleRecording() {
  const button = document.getElementById("record-btn");

  if (!isRecording) {
    // START RECORDING
    button.innerText = "🛑 Stop Recording";
    isRecording = true;

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        audioChunks = [];

        mediaRecorder.ondataavailable = event => {
          audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
          isRecording = false;
          button.innerText = "🎙 Start Recording";

          const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
          const formData = new FormData();
          formData.append("audio_data", audioBlob);

          document.getElementById("loader").style.display = "block";

          const res = await fetch("/upload", {
            method: "POST",
            body: formData
          });

          const data = await res.json();
          document.getElementById("loader").style.display = "none";

          document.getElementById("question").innerHTML = `<div class="label">You asked:</div> ${data.question}`;
          document.getElementById("response").innerHTML = `<div class="label">Philosopher says:</div> ${data.response}`;

          const utterance = new SpeechSynthesisUtterance(data.response);
          const voices = speechSynthesis.getVoices();

          const preferredVoice = voices.find(v =>
            v.name.toLowerCase().includes("male")
          );
          if (preferredVoice) {
            utterance.voice = preferredVoice;
          }

          speechSynthesis.speak(utterance);
        };
      })
      .catch(error => {
        console.error("Mic access error:", error);
        isRecording = false;
        button.innerText = "🎙 Start Recording";
      });

  } else {
    // STOP RECORDING
    if (mediaRecorder && mediaRecorder.state === "recording") {
      mediaRecorder.stop();
    }
  }
}

function stopSpeaking() {
  speechSynthesis.cancel();

  // Reset the record button state if stuck
  const button = document.getElementById("record-btn");
  if (!isRecording) {
    button.innerText = "🎙 Start Recording";
    button.disabled = false;
  }
}
