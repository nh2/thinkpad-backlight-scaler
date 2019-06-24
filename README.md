# thinkpad-backlight-scaler

Wraps `xbacklight`, scaling to a few convenient brightness steps.

Useful to bind to laptop keys to get a more pleasant darker/brighter experience.

## Similar software and resources

* The logarithmic controller in [acpilight](https://gitlab.com/wavexx/acpilight/commit/9945247b4aa7ae66464b0711e17520dbcb14bf10)
  * Would be interesting to check if its log10 covers the 4 very-low-light steps that I've [hardcoded](https://github.com/nh2/thinkpad-backlight-scaler/blob/f99db1c0cfe6e1edd992927ec19a96d2f4058c38/thinkpad-backlight-scaler.py#L14-L17) to ensure they are available.
  * https://konradstrack.ninja/blog/changing-screen-brightness-in-accordance-with-human-perception/
