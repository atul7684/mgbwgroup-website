import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "CSR & Social Activities | MGBW Group",
  description:
    "Education, Healthcare, Sustainable Livelihood, and Community Development initiatives by MGBW Group.",
};

const initiatives = [
  {
    title: "Education",
    desc: "Empowering minds through quality learning experiences",
  },
  {
    title: "HealthCare",
    desc: "Providing accessible healthcare for all communities",
  },
  {
    title: "Sustainable Livelihood",
    desc: "Creating opportunities for economic empowerment",
  },
  {
    title: "Community Development",
    desc: "Building stronger, more connected communities",
  },
];

const principles = [
  {
    num: "01",
    title: "Leading with Purpose",
    desc: "We don't stop at compliance — we aim to set new benchmarks in corporate responsibility. Our initiatives are designed to be pioneering, scalable, and transformative.",
  },
  {
    num: "02",
    title: "Impactful",
    desc: "Interventions focus on creating tangible impact — from empowering 80,000 women with sustainable livelihoods to establishing comprehensive healthcare infrastructure in underserved regions.",
  },
  {
    num: "03",
    title: "Linked to Business",
    desc: "All CSR activities leverage our organizational strengths and expertise while ensuring community benefits remain paramount.",
  },
  {
    num: "04",
    title: "Relevant to National & Local Contexts",
    desc: "CSR initiatives are deeply aligned with local contexts, promoting Kannada literature, Yakshagana performances, and Uttara Kannada folk culture.",
  },
  {
    num: "05",
    title: "Sustainable Development Principles",
    desc: "All interventions follow sustainable development principles, factoring social equity, human rights, gender inclusivity, and environmental impacts.",
  },
  {
    num: "06",
    title: "Participative & Bottom-up",
    desc: "Programs are designed with community participation at their core, ensuring relevance and ownership at the grassroots level.",
  },
  {
    num: "07",
    title: "Focused on the Disadvantaged",
    desc: "Special emphasis on reaching underprivileged communities, rural populations, women entrepreneurs, and marginalized groups.",
  },
  {
    num: "08",
    title: "Strategic & Built to Last",
    desc: "All CSR initiatives are designed to ensure communities can sustain programs beyond our direct involvement.",
  },
  {
    num: "09",
    title: "Partnerships",
    desc: "All interventions are implemented through strategic partnerships with NGOs, local authorities, government institutions, and community groups.",
  },
  {
    num: "10",
    title: "Opportunities for Volunteering",
    desc: "CSR initiatives provide diverse volunteering opportunities for employees — from educational mentoring to cultural event organization.",
  },
];

export default function ActivitiesPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gray-900 text-white py-20 text-center">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">Our Initiatives</h1>
        <p className="text-lg font-light opacity-80">
          CSR &amp; Social Activities
        </p>
      </section>

      {/* Initiatives Grid */}
      <section className="py-16 px-4 bg-white">
        <div className="max-w-4xl mx-auto grid sm:grid-cols-2 gap-6">
          {initiatives.map((init) => (
            <div
              key={init.title}
              className="bg-gray-50 rounded-xl p-8 text-center hover:shadow-md transition"
            >
              <h3 className="text-xl font-bold mb-3">{init.title}</h3>
              <p className="text-gray-600">{init.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 10 Core Principles */}
      <section className="py-20 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4">
            10 Core Principles of CSR at MGBW Group
          </h2>
          <p className="text-center text-gray-600 mb-12 max-w-2xl mx-auto">
            Our core CSR principles drive us to implement effective initiatives
            and create a positive impact in society.
          </p>
          <div className="space-y-6">
            {principles.map((p) => (
              <div
                key={p.num}
                className="bg-white rounded-xl p-6 shadow-sm flex gap-6"
              >
                <span className="text-4xl font-bold text-pink-200 shrink-0">
                  {p.num}
                </span>
                <div>
                  <h3 className="font-bold text-lg mb-2">{p.title}</h3>
                  <p className="text-gray-600 text-sm leading-relaxed">
                    {p.desc}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-pink-600 text-white text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">
          Have questions or need more information?
        </h2>
        <Link
          href="/contact"
          className="inline-block mt-4 px-8 py-3 bg-white text-pink-600 rounded-full font-semibold hover:bg-gray-100 transition"
        >
          CONTACT US
        </Link>
      </section>
    </>
  );
}
