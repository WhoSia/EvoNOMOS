require 'json'
require 'fileutils'

def target(*args, **kwargs)
  [args, kwargs]
end

def unmarked_direct(*args)
  target(*args)
end

def marked_direct(*args)
  target(*args)
end
ruby2_keywords :marked_direct

def bridge(*args)
  target(*args)
end

def marked_wrapper(*args)
  bridge(*args)
end
ruby2_keywords :marked_wrapper

def explicit_forward(*args, **kwargs)
  target(*args, **kwargs)
end

cases = {
  "UNMARKED_IMPLICIT_CONTROL" => unmarked_direct(a: 1),
  "MARKED_IMPLICIT_DIRECT" => marked_direct(a: 1),
  "MARKED_WRAPPER_GAP" => marked_wrapper(a: 1),
  "EXPLICIT_KWARGS" => explicit_forward(a: 1)
}

def preserved?(result)
  args, kwargs = result
  args.empty? && kwargs == {a: 1}
end

out = {}
cases.each do |name, result|
  out[name] = {
    "args" => result[0],
    "kwargs" => result[1],
    "preservation" => preserved?(result) ? 1 : 0
  }
end

expected = {
  "UNMARKED_IMPLICIT_CONTROL" => 0,
  "MARKED_IMPLICIT_DIRECT" => 1,
  "MARKED_WRAPPER_GAP" => 0,
  "EXPLICIT_KWARGS" => 1
}

pass = expected.all? { |k,v| out.dig(k,"preservation") == v }
payload = {
  "tool" => "ruby",
  "ruby_version" => RUBY_VERSION,
  "status" => pass ? "PASS" : "FAIL",
  "cases" => out,
  "expected" => expected,
  "separator" => {
    "same_binary_trigger_states" => ["MARKED_IMPLICIT_DIRECT","MARKED_WRAPPER_GAP"],
    "observed_preservation" => [
      out.dig("MARKED_IMPLICIT_DIRECT","preservation"),
      out.dig("MARKED_WRAPPER_GAP","preservation")
    ],
    "equal" => out.dig("MARKED_IMPLICIT_DIRECT","preservation") == out.dig("MARKED_WRAPPER_GAP","preservation")
  }
}
FileUtils.mkdir_p("out-p20")
File.write(ARGV[0] || "out-p20/p20-ruby.json", JSON.pretty_generate(payload) + "\n")
puts "P20_RUBY_SEPARATOR=#{pass ? 'PASS' : 'FAIL'}"
puts "DIRECT=#{out.dig('MARKED_IMPLICIT_DIRECT','preservation')}"
puts "WRAPPER=#{out.dig('MARKED_WRAPPER_GAP','preservation')}"
puts "EXPLICIT=#{out.dig('EXPLICIT_KWARGS','preservation')}"
puts "UNMARKED=#{out.dig('UNMARKED_IMPLICIT_CONTROL','preservation')}"
exit(pass ? 0 : 2)
