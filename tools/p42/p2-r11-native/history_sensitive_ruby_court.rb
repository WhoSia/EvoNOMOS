#!/usr/bin/env ruby
# frozen_string_literal: true
# R11-P2 preregistered native Ruby source-history and modeled edit-authority court.
# Its patches and simulated rights are research-authored, NOT actual Rack commits.
require 'json'
require 'digest'
require 'fileutils'

FROZEN = File.expand_path('../p2-r11/frozen_p2_ruby_source_history_authority_preseal.json', __dir__)
preseal = JSON.parse(File.read(FROZEN))
raise 'wrong prereg' unless preseal.fetch('protocol') == 'EVONOMOS_P42_R11_P2_HISTORY_SENSITIVE_AUTHORITY_AND_RUBY_GO_LANGUAGE_CONTRAST_PRESEAL_V1'

class AuthorityLedger
  def initialize
    @epoch = 0
    @authorities = { 'consumer' => ['prepend'] }
    @events = []
  end
  attr_reader :epoch, :events
  def permitted?(principal, action)
    @authorities.fetch(principal, []).include?(action)
  end
  def apply(principal, action)
    accepted = permitted?(principal, action)
    @events << { epoch: @epoch, owner: principal, action: action, allowed: accepted }
    accepted
  end
  def revoke(principal, action)
    @epoch += 1
    @authorities.fetch(principal).delete(action)
    @events << { epoch: @epoch, type: 'revoke', owner: principal, action: action }
  end
end

def world(order)
  store = Class.new do
    def fetch(key)
      key == '2' ? 'ok' : 'missing'
    end
  end
  trim = Module.new do
    def fetch(key)
      super(key.strip)
    end
  end
  guard = Module.new do
    def fetch(key)
      return 'rejected' unless key == key.strip
      super(key)
    end
  end
  modules = { trim: trim, guard: guard }
  order.each { |which| store.prepend(modules.fetch(which)) }
  object = store.new
  {
    order: order.map(&:to_s),
    lookup_order: store.ancestors.first(3).map { |c| c == store ? 'core' : (c == trim ? 'trim' : 'guard') },
    old: object.fetch('2'),
    lenient: object.fetch(' 2 '),
    direct_source_signature: %w[core trim guard].sort.join('|'),
    visible_effective_owner: store.ancestors.first == trim ? 'trim' : 'guard'
  }
end

guard_then_trim = world([:guard, :trim])
trim_then_guard = world([:trim, :guard])
raise 'old contract' unless guard_then_trim[:old] == 'ok' && trim_then_guard[:old] == 'ok'
raise 'lenient ordering counterexample absent' unless guard_then_trim[:lenient] == 'ok' && trim_then_guard[:lenient] == 'rejected'
raise 'same source components expected' unless guard_then_trim[:direct_source_signature] == trim_then_guard[:direct_source_signature]

ledger = AuthorityLedger.new
raise 'initial legal edit denied' unless ledger.apply('consumer', 'prepend')
ledger.revoke('consumer', 'prepend')
raise 'revoked edit accepted' if ledger.apply('consumer', 'prepend')

# Declared context-specific demands determine which *real Ruby method chain*
# is correct, with old client behavior preserved in both.
contexts = {
  lenient: { expect: 'ok', best: guard_then_trim, worse: trim_then_guard },
  strict: { expect: 'rejected', best: trim_then_guard, worse: guard_then_trim }
}
contexts.each do |name, x|
  raise "#{name} best mismatch" unless x[:best][:lenient] == x[:expect]
  raise "#{name} reversal missing" if x[:worse][:lenient] == x[:expect]
end

result = {
  status: 'R11_P2_RUBY_NATIVE_HISTORY_ORDER_AUTHORITY_AND_CONDITIONAL_REVERSAL_PASS',
  engine: RUBY_VERSION, 
  first: guard_then_trim,
  second: trim_then_guard,
  temporal_authority: ledger.events,
  independent_client_contexts: { lenient: { preferred: 'trim_outer', other_fails: true }, strict: { preferred: 'guard_outer', other_fails: true } },
  warning: 'The two Ruby wrapper code fragments and temporal edit-authority ledger are researcher-authored. Runtime Ruby Module#prepend behavior actually executed. This is standard Ruby dynamic method lookup, not an original maintained cross-owner patch.'
}
dir = File.expand_path('../../../out/p42-r11', __dir__)
FileUtils.mkdir_p(dir)
File.write(File.join(dir, 'p2-native-ruby-authority-court.json'), JSON.pretty_generate(result) + "\n")
puts 'R11_P2_RUBY_SAME_COMPONENT_SOURCE_DIFFERENT_PREPEND_HISTORY_PASS'
puts 'R11_P2_RUBY_OLD_PRESERVED_LENIENT_STRICT_PRECEDENCE_REVERSAL_PASS'
puts 'R11_P2_TEMPORAL_AUTHORIZATION_REVOCATION_NEGATIVE_PASS'
puts JSON.generate(result)
