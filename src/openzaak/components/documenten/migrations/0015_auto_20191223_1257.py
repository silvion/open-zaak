# Generated by Django 2.2.4 on 2019-12-23 12:57

from django.db import migrations, models
import django_loose_fk.fields


class Migration(migrations.Migration):

    dependencies = [
        ("documenten", "0014_auto_20191223_1132"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="objectinformatieobject", name="check_type",
        ),
        migrations.RemoveConstraint(
            model_name="objectinformatieobject", name="unique_io_zaak",
        ),
        migrations.RemoveConstraint(
            model_name="objectinformatieobject", name="unique_io_besluit",
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="besluit",
            field=django_loose_fk.fields.FkOrURLField(
                blank=True, fk_field="_besluit", null=True, url_field="_besluit_url"
            ),
        ),
        migrations.AddField(
            model_name="objectinformatieobject",
            name="zaak",
            field=django_loose_fk.fields.FkOrURLField(
                blank=True, fk_field="_zaak", null=True, url_field="_zaak_url"
            ),
        ),
        migrations.AddConstraint(
            model_name="objectinformatieobject",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        models.Q(
                            models.Q(("_zaak__isnull", False), ("_zaak_url", "")),
                            models.Q(
                                models.Q(_negated=True, _zaak_url=""),
                                ("_zaak__isnull", True),
                            ),
                            _connector="OR",
                        ),
                        ("_besluit__isnull", True),
                        ("_besluit_url", ""),
                        ("object_type", "zaak"),
                    ),
                    models.Q(
                        models.Q(
                            models.Q(("_besluit__isnull", False), ("_besluit_url", "")),
                            models.Q(
                                models.Q(_besluit_url="", _negated=True),
                                ("_besluit__isnull", True),
                            ),
                            _connector="OR",
                        ),
                        ("_zaak__isnull", True),
                        ("_zaak_url", ""),
                        ("object_type", "besluit"),
                    ),
                    _connector="OR",
                ),
                name="check_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="objectinformatieobject",
            constraint=models.UniqueConstraint(
                fields=("informatieobject", "_zaak"), name="unique_io_zaak_local"
            ),
        ),
        migrations.AddConstraint(
            model_name="objectinformatieobject",
            constraint=models.UniqueConstraint(
                condition=models.Q(_negated=True, _zaak_url=""),
                fields=("informatieobject", "_zaak_url"),
                name="unique_io_zaak_external",
            ),
        ),
        migrations.AddConstraint(
            model_name="objectinformatieobject",
            constraint=models.UniqueConstraint(
                fields=("informatieobject", "_besluit"), name="unique_io_besluit_local"
            ),
        ),
        migrations.AddConstraint(
            model_name="objectinformatieobject",
            constraint=models.UniqueConstraint(
                condition=models.Q(_besluit_url="", _negated=True),
                fields=("informatieobject", "_besluit_url"),
                name="unique_io_besluit_external",
            ),
        ),
    ]