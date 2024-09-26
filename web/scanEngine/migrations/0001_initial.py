# Generated by Django 3.2.4 on 2021-12-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('engine_name', models.CharField(max_length=200)),
                ('subdomain_discovery', models.BooleanField()),
                ('dir_file_fuzz', models.BooleanField()),
                ('port_scan', models.BooleanField()),
                ('fetch_url', models.BooleanField()),
                ('vulnerability_scan', models.BooleanField(default=False, null=True)),
                ('osint', models.BooleanField(default=False, null=True)),
                ('screenshot', models.BooleanField(default=True, null=True)),
                ('yaml_configuration', models.TextField()),
                ('default_engine', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hackerone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('api_key', models.CharField(blank=True, max_length=200, null=True)),
                ('send_critical', models.BooleanField(default=True)),
                ('send_high', models.BooleanField(default=True)),
                ('send_medium', models.BooleanField(default=False)),
                ('report_template', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstalledExternalTool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('logo_url', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('github_url', models.CharField(max_length=80)),
                ('license_url', models.CharField(blank=True, max_length=100, null=True)),
                ('version_lookup_command', models.CharField(blank=True, max_length=100, null=True)),
                ('update_command', models.CharField(blank=True, max_length=200, null=True)),
                ('install_command', models.CharField(max_length=200)),
                ('version_match_regex', models.CharField(blank=True, default='[vV]*(\\d+\\.)?(\\d+\\.)?(\\*|\\d+)', max_length=100, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('is_subdomain_gathering', models.BooleanField(default=False)),
                ('is_github_cloned', models.BooleanField(default=False)),
                ('github_clone_path', models.CharField(blank=True, max_length=100, null=True)),
                ('subdomain_gathering_command', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterestingLookupModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('custom_type', models.BooleanField(default=False)),
                ('title_lookup', models.BooleanField(default=True)),
                ('url_lookup', models.BooleanField(default=True)),
                ('condition_200_http_lookup', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_to_slack', models.BooleanField(default=False)),
                ('send_to_discord', models.BooleanField(default=False)),
                ('send_to_telegram', models.BooleanField(default=False)),
                ('slack_hook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('discord_hook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('telegram_bot_token', models.CharField(blank=True, max_length=100, null=True)),
                ('telegram_bot_chat_id', models.CharField(blank=True, max_length=100, null=True)),
                ('send_scan_status_notif', models.BooleanField(default=True)),
                ('send_interesting_notif', models.BooleanField(default=True)),
                ('send_vuln_notif', models.BooleanField(default=True)),
                ('send_subdomain_changes_notif', models.BooleanField(default=True)),
                ('send_scan_output_file', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('use_proxy', models.BooleanField(default=False)),
                ('proxies', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VulnerabilityReportSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primary_color', models.CharField(blank=True, default='#FFB74D', max_length=10, null=True)),
                ('secondary_color', models.CharField(blank=True, default='#212121', max_length=10, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_address', models.CharField(blank=True, max_length=200, null=True)),
                ('company_email', models.CharField(blank=True, max_length=100, null=True)),
                ('company_website', models.CharField(blank=True, max_length=100, null=True)),
                ('show_rengine_banner', models.BooleanField(default=True)),
                ('show_executive_summary', models.BooleanField(default=True)),
                ('executive_summary_description', models.TextField(blank=True, null=True)),
                ('show_footer', models.BooleanField(default=False)),
                ('footer_text', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wordlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
