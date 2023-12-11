#!/usr/bin/env ruby
# The above line specifies that the script should be interpreted by the Ruby interpreter.

# Output the substring that matches the regular expression /hbt{2,5}n/
puts ARGV[0].scan(/hbt{2,5}n/).join
