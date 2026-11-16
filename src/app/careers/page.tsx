import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Careers at MGBW Group | Join Our Legacy of Excellence",
  description:
    "Build with purpose, grow with us. Explore career opportunities at MGBW Group.",
};

const values = [
  {
    title: "Our People",
    desc: "At MGBW, we see our team as family. Collaboration, respect, and shared growth form the foundation of everything we do. Every role — from skilled artisans to management — is valued.",
  },
  {
    title: "Commitment to Quality",
    desc: "Excellence is at the heart of MGBW. We hold ourselves to the highest standards, ensuring that every product and service reflects the consistency and care we are known for.",
  },
  {
    title: "Community Impact",
    desc: "We believe business is meaningful only when it uplifts. Our efforts support local communities, preserve traditional skills, and create livelihoods that endure across generations.",
  },
];

export default function CareersPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gray-900 text-white py-20 text-center px-4">
        <h1 className="text-4xl md:text-5xl font-bold mb-6">
          Build With Purpose. Grow With Us.
        </h1>
        <p className="text-lg font-light opacity-80 max-w-3xl mx-auto leading-relaxed">
          At <strong>MGBW Group</strong>, people are at the heart of everything
          we do. For over eight decades, we&apos;ve grown across industries by
          fostering trust, discipline, responsibility, quality, and innovation —
          not only in our businesses but also in the teams that drive them.
        </p>
      </section>

      {/* Intro */}
      <section className="py-16 px-4 bg-white">
        <div className="max-w-3xl mx-auto text-center">
          <p className="text-gray-600 text-lg leading-relaxed">
            We believe in creating opportunities where talent thrives, ideas are
            valued, and contributions make a real impact. Whether in
            manufacturing, hospitality, fragrance, or emerging ventures, working
            with MGBW means being part of an organization that blends tradition
            with forward-looking growth.
          </p>
        </div>
      </section>

      {/* Values */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto grid md:grid-cols-3 gap-8">
          {values.map((v) => (
            <div key={v.title} className="bg-white rounded-xl p-8 shadow-sm">
              <h3 className="text-xl font-bold mb-4">{v.title}</h3>
              <p className="text-gray-600 text-sm leading-relaxed">{v.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Application Form */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-2xl mx-auto">
          <h2 className="text-3xl font-bold mb-4 text-center">
            Join Our Journey
          </h2>
          <p className="text-gray-600 text-center mb-8">
            While we are not actively hiring at this moment, we are always keen
            to connect with passionate individuals who want to grow with us.
            Share your profile and we&apos;ll reach out when opportunities arise.
          </p>
          <div className="bg-gray-50 rounded-2xl p-8">
            <p className="text-center text-gray-700 mb-4">
              Send your resume to:
            </p>
            <a
              href="mailto:hr@mgbw501.com"
              className="block text-center text-2xl font-bold text-pink-600 hover:underline"
            >
              hr@mgbw501.com
            </a>
            <p className="text-center text-sm text-gray-500 mt-2">
              PDF format preferred, max 5MB
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
