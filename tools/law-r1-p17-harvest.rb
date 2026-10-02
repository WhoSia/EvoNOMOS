require 'json'
require 'fileutils'

input = ARGV[0] || 'active/g8-law-r1-p17/P17_HARVEST_LR-20261002-V.json'
output = ARGV[1] || 'out-p17/ruby-harvest.json'
d = JSON.parse(File.read(input))

checks = {
  'non_sovereign' => d['status'] == 'HARVEST_ONLY_NON_SOVEREIGN',
  'authority_none' => d['authority_transferred_to_p17'] == 'NONE',
  'fragment_count' => d.fetch('fragments', []).length >= 8,
  'kill_count' => d.fetch('kill_fragments', []).length >= 4,
  'paper_seeds' => d.fetch('paper_seeds', []).length >= 3,
  'cross_lab_backflow' => d.fetch('cross_lab_backflow', []).length >= 4,
  'acquisition_open' => d.fetch('acquisition_open', []).length >= 3
}
pass = checks.values.all?
FileUtils.mkdir_p('out-p17')
File.write(output, JSON.pretty_generate({
  'tool' => 'ruby',
  'status' => pass ? 'PASS_HARVEST_NON_SOVEREIGN' : 'FAIL',
  'checks' => checks,
  'paper_seed_ids' => d.fetch('paper_seeds', []).map{|x| x['id']},
  'authority_transferred' => d['authority_transferred_to_p17']
}) + "\n")
puts 'P17_RUBY_HARVEST=' + (pass ? 'PASS' : 'FAIL')
exit(pass ? 0 : 4)
