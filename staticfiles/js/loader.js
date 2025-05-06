// wait until the entire page has loaded
window.addEventListener('load', function() {
	// fade out the preloader
	document.getElementById('preloader').style.opacity = '0';

	// remove the preloader from the DOM after the fadeOut effect
	setTimeout(function() {
		document.getElementById('preloader').style.display = 'none'
	}, 500); // adjust tie to specific fade-out time
});