#!/usr/bin/env ruby

def extract_info(log_line)
  # Regular expression to extract information from the log line
  regex = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/

  # Match the regular expression with the log line
  match = log_line.match(regex)

  if match
    sender = match[:sender]
    receiver = match[:receiver]
    flags = match[:flags]
    "#{sender},#{receiver},#{flags}"
  else
    "Invalid log entry"
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: ./100-textme.rb <log_file>"
else
  # Get the log file path from the command line argument
  log_file_path = ARGV[0]

  # Read the log file and process each line
  File.foreach(log_file_path) do |line|
    # Check if the line contains "Receive SMS" or "Sent SMS"
    if line.include?("Receive SMS") || line.include?("Sent SMS")
      result = extract_info(line)
      puts result
    end
  end
end
