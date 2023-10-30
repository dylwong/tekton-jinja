FROM registry.access.redhat.com/ubi9/ubi-minimal:9.2

RUN microdnf install python36 curl which
# && microdnf update \
# && microdnf clean all

WORKDIR /opt/tekton-generate

COPY render.py /opt/tekton-generate/src/
COPY Pipfile /opt/tekton-generate/pyenv/
COPY render stage /opt/tekton-generate/bin/

ENV LANG="C.UTF-8" \
    LC_ALL="C.UTF-8" \
    LC_CTYPE="C.UTF-8" \
    WORKON_HOME=/opt/tekton-generate/pyenv \
    PIPENV_NOSPIN=1

RUN pip3 install pipenv \
 && cd /opt/tekton-generate/pyenv \
 && pipenv --python 3.6 install \
 && chown -R 9999:0 /opt/tekton-generate \
 && chmod -R g+rwX /opt/tekton-generate

# emulate an anonymous uid, which is better aligned with OpenShift environment
USER 9999

CMD [ "echo", "No default command" ]
