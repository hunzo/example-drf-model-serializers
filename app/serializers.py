from rest_framework import serializers
from .models import Payload, AttachFile


class AttacheFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachFile
        fields = '__all__'


class PayloadSerializers(serializers.ModelSerializer):

    attach_files = AttacheFileSerializer(many=True)

    class Meta:
        model = Payload
        fields = '__all__'
        depth = 1

    def create(self, validate_data):
        attach_files = validate_data.pop("attach_files")
        payload_instance = Payload.objects.create(**validate_data)
        for attFile in attach_files:
            AttachFile.objects.create(payload=payload_instance, **attFile)
        return payload_instance

    def update(self, instance, validate_data):
        attach_files_list = validate_data.pop("attach_files")
        instance.content_html = validate_data.get(
            "content_html", instance.content_html)
        instance.subject = validate_data.get("subject", instance.subject)
        instance.to_recipients = validate_data.get(
            "to_recipients", instance.to_recipients)
        instance.save()

        attfile_with_same_payload = AttachFile.objects.filter(
            payload=instance.pk).values_list("id", flat=True)

        files_id_pool = []
        for f in attach_files_list:
            if 'id' in f.keys():
                if AttachFile.objects.filter(id=f["id"]).exists():
                    file_instance = AttachFile.objects.get(id=f["id"])
                    file_instance.file_bytes = f.get(
                        "file_bytes", file_instance.file_bytes)
                    file_instance.name = f.get("name", file_instance.name)
                    file_instance.isInline = f.get(
                        "isInline", file_instance.isInline)
                    file_instance.content_id = f.get(
                        "content_id", file_instance.content_id)
                    file_instance.save()
                    files_id_pool.append(file_instance.id)
                else:
                    continue
            else:
                file_instance = AttachFile.objects.create(
                    payload=instance, **f)
                files_id_pool.append(file_instance.id)

        for file_id in attfile_with_same_payload:
            if file_id not in files_id_pool:
                AttachFile.objects.filter(pk=file_id).delete()

        return instance
