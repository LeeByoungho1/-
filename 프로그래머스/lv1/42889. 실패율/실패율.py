def solution(N, stages):
    failure_rates = {}
    total_players = len(stages)
    
    # Calculate the failure rate for each stage
    for stage in range(1, N+1):
        players_in_stage = stages.count(stage)
        if total_players > 0:
            failure_rate = players_in_stage / total_players
        else:
            failure_rate = 0
        failure_rates[stage] = failure_rate
        total_players -= players_in_stage
    
    # Sort the stages by their failure rates
    return sorted(failure_rates, key=lambda x: failure_rates[x], reverse=True)
