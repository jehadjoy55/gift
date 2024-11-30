function openGift() {
  const lid = document.querySelector('.box-lid');
  const poem = document.getElementById('poem');
  const audio = document.getElementById('giftAudio');

  // Open the lid
  lid.classList.add('open');

  // Show the poem
  poem.classList.add('visible');

  // Play the audio
  audio.play();
}
