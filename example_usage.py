from client import PhysicsMorphingGenerativeVideoFxClient

def main():
    client = PhysicsMorphingGenerativeVideoFxClient()
    res = client.apply_generative_physics_effect('https://assets.genpark.ai/images/sports_car.png', 'INFLATE_BALLOON_POP', 8)
    print('Effect Job: ' + res['effect_job_id'] + ' (' + res['effect_applied'] + ')')
    print('Mass Conservation: ' + str(res['volumetric_mass_conservation_pct']) + '% | Surface Tension: ' + str(res['surface_tension_fidelity_score']) + '%')
    print('FX Video URL: ' + res['rendered_fx_video_url'] + ' | Alpha: ' + str(res['alpha_transparency_channel_ready']))

if __name__ == '__main__':
    main()
