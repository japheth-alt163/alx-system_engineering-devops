#!/usr/bin/env ruby
# The above line specifies that the script should be interpreted by the Ruby interpreter.

# Output the substring that matches the regular expression /hbt*n/
puts ARGV[0].scan(/hbt*n/).join
