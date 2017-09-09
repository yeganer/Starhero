In order to record voice to `.wav` install the `sox` package.

linux via apt-get:   `sudo apt-get install sox`
mac via homebrew:    `brew install sox`

(sorry windows users)

to record sound once 4% of max input sensitivity is reached and stop when it is again <4% max input for one second:
`rec temp.wav silence 1 5 4% 1 0:00:01 4%`


