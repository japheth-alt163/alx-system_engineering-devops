#!/usr/bin/env ruby
# The above line specifies that the script should be interpreted by the Ruby interpreter.

# Output the substrings that match the regular expression /(?<=from:|to:|flags:).+?(?=\])/
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(",")
