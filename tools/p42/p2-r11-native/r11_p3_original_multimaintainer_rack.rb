#!/usr/bin/env ruby
# frozen_string_literal: true
# Native tests use UNMODIFIED original rack/rack source at an exact Git commit.
# All observers are research tests; no assertion that legacy expressive caller existed in upstream.
require 'json'
phase = ARGV.fetch(0)
raise "bad phase" unless %w[early mid late].include?(phase)
require 'rack/builder'
Builder = Rack::Builder

app = ->(_env) { [200, {'content-type'=>'text/plain'}, ['original-rack-body']] }
calls = []
tracer = TracePoint.new(:call) do |t|
  if t.defined_class.to_s.start_with?('Rack::') && %w[run to_app call use map].include?(t.method_id.to_s)
    calls << "#{t.defined_class}##{t.method_id}"
  end
end
b = Builder.new
rv = nil
response = nil
tracer.enable do
  rv = b.run(app)
  response = b.to_app.call({'rack.version'=>[3,0],'REQUEST_METHOD'=>'GET','PATH_INFO'=>'/','SCRIPT_NAME'=>'','QUERY_STRING'=>''})
end
raise 'original Rack existing app failed' unless response[0]==200 && response[2].to_a==['original-rack-body']

has_options = b.respond_to?(:options)
opts_ok = if has_options
            Builder.new(foo: :bar).options[:foo] == :bar
          else
            false
          end
exp = {
  'early'=>[false,true,false],
  'mid'=>[true,true,false],
  'late'=>[true,false,true]
}.fetch(phase)
observed = [opts_ok,rv.equal?(app),rv.nil?]
raise "original Ruby observation #{phase} #{observed} != #{exp}" unless observed==exp

# Original DSL receiver behavior: syntax and call response safe in all snapshots,
# expression return-value changes in actual late source.
mw = Class.new do
  def initialize(inner, tag: nil)
    @inner, @tag = inner, tag
  end
  def call(env)
    status,headers,body=@inner.call(env)
    headers= headers.merge('x-original-wrapper'=>@tag.to_s)
    [status,headers,body]
  end
end
builder_mw=Builder.new
use_rv=builder_mw.use(mw,tag:'native')
builder_mw.run(app)
wrapped=builder_mw.to_app.call({'rack.version'=>[3,0],'REQUEST_METHOD'=>'GET','PATH_INFO'=>'/','SCRIPT_NAME'=>''})
raise 'original Rack keyword middleware delegation fails' unless wrapped[1]['x-original-wrapper']=='native'
raise 'DSL use must return nil only in late' unless use_rv.nil? == (phase=='late')

m=Builder.new
map_rv=m.map('/hello') { run app }
raise 'DSL map must return nil only in late' unless map_rv.nil? == (phase=='late')

out={
 phase:phase,
 original_rack_source_location:Builder.instance_method(:run).source_location,
 lookup_constructor_parameters:Builder.instance_method(:initialize).parameters,
 exposed_api_parameters:Builder.method(:new_from_string).parameters,
 original_rack_runtime_call_trace:calls,
 initial_contract_status:response[0],
 old_consumer_ignored_return:true,
 new_keyword_builder_options:opts_ok,
 expressive_return_app_identity:rv.equal?(app),
 command_style_return_nil:rv.nil?,
 middleware_original_keyword_dispatch:true,
 middleware_use_return_nil:use_rv.nil?,
 map_return_nil:map_rv.nil?,
 source_is_unmodified:true,
 authorial_client_observer_status:'research-authored; does not demonstrate a real public dependent app'
}
puts "R11_P3_NATIVE_ORIGINAL_RACK_#{phase.upcase}_PREDICTIONS_MATCH"
puts JSON.generate(out)
